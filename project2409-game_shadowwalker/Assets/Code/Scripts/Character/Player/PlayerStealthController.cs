using UnityEngine;
using UnityEngine.Events;

public class PlayerStealthController : MonoBehaviour 
{
    public InRangeOfEnemyEvent inRangeOfEnemy;
    public UnityEvent notInRangeOfEnemy;
    public UnityEvent playerIsTakingDown;
    public InHearingRangeOfEnemyEvent inHearingRangeOfEnemyEvent;

    private HUD hud;
    private CharacterAnimationController characterAnimationController;
    private PlayerInputController playerInputController;
    private PlayerMovementController playerMovementController;

    void Awake()
    {
        hud = GameObject.FindGameObjectWithTag("HUD").GetComponent<HUD>();
        characterAnimationController = GetComponent<CharacterAnimationController>();
        playerInputController = GetComponent<PlayerInputController>();
        playerMovementController = GetComponent<PlayerMovementController>();
    }
    
    void Start()
    {
        inRangeOfEnemy = new InRangeOfEnemyEvent();
        inRangeOfEnemy.AddListener(HandleInRangeOfEnemyEvent);

        notInRangeOfEnemy = new UnityEvent();
        notInRangeOfEnemy.AddListener(HandleNotInRangeOfEnemyEvent);

        inHearingRangeOfEnemyEvent = new InHearingRangeOfEnemyEvent();
        inHearingRangeOfEnemyEvent.AddListener(HandleInHearingRangeOfEnemyEvent);
    }

    private void HandleInHearingRangeOfEnemyEvent(EnemyController enemyController)
    {
        if (!characterAnimationController.IsCrouching())
        {
            if (playerMovementController.GetHorizontalVelocity() > PlayerMovementController.WalkingVelocity)
            {
                enemyController.noiseEvent.Invoke(enemyController, this.transform.position);
            }
            else if (playerMovementController.GetHorizontalVelocity() > PlayerMovementController.IdleVelocity &&
                     Vector3.Distance(transform.position, enemyController.transform.position) < enemyController.enemyStateMachine.enemyPatrolState.hearingRadius / 2)
            {
                enemyController.noiseEvent.Invoke(enemyController, this.transform.position); 
            }
        }
    }

    void Update()
    {
        
    }

    private void HandleInRangeOfEnemyEvent(EnemyController enemyController)
    {
        hud.EnableTakedownPrompt();
        if (playerInputController.IsTakingDown()) {
            enemyController.isBeingTakenDown.Invoke();
            hud.DisableTakedownPrompt();
            characterAnimationController.SetTakingDown(true);
        }
    }

    private void HandleNotInRangeOfEnemyEvent()
    {
        hud.DisableTakedownPrompt();
    }
}