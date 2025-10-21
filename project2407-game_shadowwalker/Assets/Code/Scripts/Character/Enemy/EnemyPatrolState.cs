using System.Security.Cryptography.X509Certificates;
using UnityEngine;
using UnityEngine.AI;
using UnityEngine.Events;

public class EnemyPatrolState : IState
{
    private EnemyController enemyController;
    private int nextPatrolWaypoint = -1;
    private int time = 0;
    private int delayAtDestination = 2000;
    public float hearingRadius = 4.0f;
    private bool isInvestigatingNoise = false;

    public EnemyPatrolState(EnemyController enemyController)
    {
        this.enemyController = enemyController;
    }

    public void Enter()
    {
        Debug.Log("Entering EnemyPatrol State");

        enemyController.navMeshAgent.speed = 0.4f;
        SetNextPatrolWaypoint();
    }

    public void Exit()
    {
        Debug.Log("Exiting EnemyPatrol State");
    }

    public void Update()
    {
        (bool canSeeDeadEnemy, Vector3 position) = enemyController.CanSeeDeadEnemy();
        if (enemyController.CanSeeCharacter())
        {
            enemyController.enemyStateMachine.ChangeState(enemyController.enemyStateMachine.enemyDetectedState);
        }
        else if (canSeeDeadEnemy)
        {
            enemyController.enemyStateMachine.enemyAlertState.AddAlertWayPoint(position);
            enemyController.enemyStateMachine.ChangeState(enemyController.enemyStateMachine.enemyAlertState);
        }
        else if (HasReachedNextDestination() && Wait())
        {
            SetNextPatrolWaypoint();
            isInvestigatingNoise = false;
        }
        // Else If enemy hears player but player is not in view, switch to Alert state with location of sound as the target location
    }

    private void SetNextPatrolWaypoint()
    {
        if (enemyController.patrolPath.Length > 0)
        {
            if (!isInvestigatingNoise)
            {
                nextPatrolWaypoint++;
            }
            Transform[] patrolPath = enemyController.patrolPath;
            int patrolPathLen = enemyController.patrolPath.Length;
            Vector3 nextPatrolWaypointPosition = patrolPath[nextPatrolWaypoint % patrolPathLen].transform.position;
            enemyController.navMeshAgent.SetDestination(nextPatrolWaypointPosition);
        }
    }

    private bool HasReachedNextDestination()
    {
        NavMeshAgent navMeshAgent = enemyController.navMeshAgent;
        return !navMeshAgent.pathPending && navMeshAgent.remainingDistance <= navMeshAgent.stoppingDistance;
    }

    private bool Wait() {
        if (time == delayAtDestination) {
            time = 0;
            return true;
        } else {
            time++;
            enemyController.navMeshAgent.SetDestination(enemyController.transform.position);
            return false;
        }
    }

    public void HandleNoiseEvent(EnemyController enemyController, Vector3 noiseLocation)
    {
        if (!isInvestigatingNoise && Vector3.Distance(enemyController.transform.position, noiseLocation) < hearingRadius)
        {
            isInvestigatingNoise = true;
            NavMeshAgent navMeshAgent = enemyController.navMeshAgent;
            navMeshAgent.SetDestination(noiseLocation);
        }
    }
}