using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class EnemyAlertState : IState
{
    public Queue<Vector3> alertPositions;
    private EnemyController enemyController;
    private int time = 0;
    private int delayAtWaypoint = 4000;
    public EnemyAlertState(EnemyController enemyController)
    {
        this.enemyController = enemyController;
        this.alertPositions = new Queue<Vector3>();
    }

    public void Enter()
    {
        Debug.Log("Entering Alert State");
        enemyController.navMeshAgent.speed = 1.0f;
        enemyController.navMeshAgent.SetDestination(alertPositions.Dequeue());
    }

    public void Exit()
    {
        Debug.Log("Exiting Alert State");
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
            AddAlertWayPoint(position);
        }
        SetAlertWayPoint();
        // If player is in view, game over
        // Else if alert location not reached, RUN towards 
            // If another alert is received, change target
        // Else if alert location iis reached, return to Patrol state
    }

    public void AddAlertWayPoint(Vector3 position)
    {
        alertPositions.Enqueue(position);
    }

    private void SetAlertWayPoint()
    {
        if (HasReachedAlertWaypoint())
        {
            if (alertPositions.Count > 0)
            {
                if (Wait())
                {
                    Debug.Log("Reached alert waypoint");
                    enemyController.navMeshAgent.SetDestination(alertPositions.Dequeue());
                }
            } 
            else
            {
                enemyController.enemyStateMachine.ChangeState(enemyController.enemyStateMachine.enemyPatrolState);
            }
        }
    }

    private bool HasReachedAlertWaypoint()
    {
        NavMeshAgent navMeshAgent = enemyController.navMeshAgent;
        return !navMeshAgent.pathPending && navMeshAgent.remainingDistance <= navMeshAgent.stoppingDistance;
    }

    private bool Wait() {
        if (time == delayAtWaypoint) {
            time = 0;
            return true;
        } else {
            time++;
            enemyController.navMeshAgent.SetDestination(enemyController.transform.position);
            return false;
        }
    }
}