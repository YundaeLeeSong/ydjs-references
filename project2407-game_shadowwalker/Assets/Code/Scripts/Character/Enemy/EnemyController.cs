using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
using UnityEngine.Events;

public class EnemyController : MonoBehaviour
{
    private GameObject player;
    public Transform[] patrolPath;
    public TakedownEvent isBeingTakenDown;
    public NoiseEvent noiseEvent;
    public CharacterController characterController;

    public NavMeshAgent navMeshAgent;
    public EnemyStateMachine enemyStateMachine;
    public Animator animator;
    public bool isDead;
    public float maxVisibilityDistance = 7.5f;

    private float proximityToTriggerKill = 2.5f;
    private AudioSource walkAudioSource;
    private AudioSource jumpAudioSource;
    private AudioSource runAudioSource;
    private bool characterWasInRange = false;
    private bool playerWasSeen = false;
    private StealthManager stealthManager;
    public HashSet<GameObject> seenDeadEnemies;

    void Awake()
    {
        navMeshAgent = GetComponent<NavMeshAgent>();
        navMeshAgent.updatePosition = false;
        navMeshAgent.updateRotation = true;
        enemyStateMachine = new EnemyStateMachine(this);
        animator = GetComponent<Animator>();
        AudioSource[] audioSources = GetComponents<AudioSource>();
        jumpAudioSource = audioSources[0];
        runAudioSource = audioSources[1];
        walkAudioSource = audioSources[2];
        characterController = GetComponent<CharacterController>();
        seenDeadEnemies = new HashSet<GameObject>();
        stealthManager = GameObject.FindGameObjectWithTag("StealthManager").GetComponent<StealthManager>();

        isBeingTakenDown = new TakedownEvent();
        isBeingTakenDown.AddListener(HandleDeath);

        noiseEvent = new NoiseEvent();
        noiseEvent.AddListener(enemyStateMachine.enemyPatrolState.HandleNoiseEvent);

        player = GameObject.FindGameObjectWithTag("Player");
    }

    void Update()
    {
        CanCharacterTakeDown();
        HandlePlayerInHearingRange();
        enemyStateMachine.Update();
        animator.SetFloat("horizontalVelocity", navMeshAgent.velocity.magnitude);
        
        if (CanSeeCharacter())
        {
            if (!playerWasSeen)
            {
                playerWasSeen = true;
                stealthManager.GetDetected();
            }
        }
        else if (playerWasSeen)
        {
            playerWasSeen = false;
            stealthManager.StopDetection();
        }
    }

    private void OnAnimatorMove()
    {
        Vector3 animatorRootPosition = animator.rootPosition;
        animatorRootPosition.y = navMeshAgent.nextPosition.y;
        transform.position = animatorRootPosition;
        navMeshAgent.nextPosition = animatorRootPosition;
    }

    public void WalkEvent()
    {
        walkAudioSource.Play();
    }
    public void RunEvent()
    {
        runAudioSource.Play();
    }
    public void JumpEvent()
    {
        jumpAudioSource.Play();
    }

    public void CanCharacterTakeDown()
    {
        // Inspired by https://discussions.unity.com/t/detect-player-in-range-of-enemy/687/3 with modifications to check if player is behind the enemy
        Vector3 characterPosition = player.transform.position + player.GetComponent<CharacterController>().center;
        Vector3 enemyPosition = transform.position + characterController.center;

        Vector3 rayDirection = enemyPosition - characterPosition;

        Vector3 characterDirection = player.transform.TransformDirection(Vector3.forward);
        Vector3 oppositeEnemyDirection = transform.TransformDirection(Vector3.back);

        float fwdAngleDot = Vector3.Dot(rayDirection, characterDirection);
        bool enemyIsInLineOfSight = fwdAngleDot > 0.0;

        float bwdAngleDot = Vector3.Dot(rayDirection, oppositeEnemyDirection);
        bool playerIsBehind = bwdAngleDot < 0.0;

        bool inProximity = rayDirection.sqrMagnitude < (proximityToTriggerKill * proximityToTriggerKill);
        RaycastHit hit;
        bool raycastHitSomething = Physics.Raycast(characterPosition, rayDirection, out hit, proximityToTriggerKill);

        if (inProximity && enemyIsInLineOfSight && playerIsBehind && raycastHitSomething && hit.collider.gameObject == this.gameObject && !isDead)
        {
            player.GetComponent<PlayerStealthController>().inRangeOfEnemy.Invoke(this);
            characterWasInRange = true;
        }
        else if (characterWasInRange)
        {
            characterWasInRange = false;
            player.GetComponent<PlayerStealthController>().notInRangeOfEnemy.Invoke();
        }
    }

    public void HandleDeath()
    {
        enemyStateMachine.ChangeState(enemyStateMachine.enemyDeadState);
    }

    public bool CanSeeCharacter()
    {
        Vector3 directionToPlayer = player.transform.position - transform.position;
        Vector3 enemyDirection = transform.TransformDirection(Vector3.forward);
        float angleDot = Vector3.Dot(directionToPlayer, enemyDirection);
        bool playerInFrontOfEnemy = angleDot > 0.0;
        RaycastHit hit;
        return playerInFrontOfEnemy && Physics.Raycast(transform.position, directionToPlayer, out hit, maxVisibilityDistance) && hit.collider.gameObject.CompareTag("Player");
    }

    public (bool, Vector3) CanSeeDeadEnemy()
    {
        GameObject[] enemies = GameObject.FindGameObjectsWithTag("Enemy");
        foreach (GameObject enemy in enemies)
        {
            if (seenDeadEnemies.Contains(enemy) || enemy == this.gameObject)
                continue;

            Vector3 currPosition = transform.position + characterController.center;
            Vector3 enemyPosition = enemy.transform.position;

            Vector3 rayDirection = enemyPosition - currPosition;

            Vector3 currDirection = transform.TransformDirection(Vector3.forward);

            float fwdAngleDot = Vector3.Dot(rayDirection, currDirection);
            bool enemyIsInLineOfSight = fwdAngleDot > 0.0;
            bool inVisibility = rayDirection.sqrMagnitude < (maxVisibilityDistance * maxVisibilityDistance);
            bool raycastHitSomething = Physics.Raycast(currPosition, rayDirection, out var hit, maxVisibilityDistance);

            if (inVisibility && enemyIsInLineOfSight && raycastHitSomething && hit.collider.gameObject == enemy && enemy.GetComponent<EnemyController>().isDead)
            {
                seenDeadEnemies.Add(enemy);
                return (true, hit.collider.gameObject.transform.position);
            }
        }
        return (false, new Vector3());
    }

    private void HandlePlayerInHearingRange()
    {
        if (Vector3.Distance(transform.position, player.transform.position) < enemyStateMachine.enemyPatrolState.hearingRadius)
        {
            player.GetComponent<PlayerStealthController>().inHearingRangeOfEnemyEvent.Invoke(this);
        }
    }
}
