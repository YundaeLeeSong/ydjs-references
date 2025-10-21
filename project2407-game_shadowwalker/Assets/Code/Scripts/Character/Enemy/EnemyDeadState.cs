using UnityEngine;

public class EnemyDeadState : IState
{
    private EnemyController enemyController;

    public EnemyDeadState(EnemyController enemyController)
    {
        this.enemyController = enemyController;
    }

    public void Enter()
    {
        Debug.Log("Entering Dead State");
        enemyController.isDead = true;
        enemyController.navMeshAgent.updateRotation = false;
        // enemyController.GetComponent<BoxCollider>().enabled = false;
        // enemyController.GetComponent<CharacterController>().enabled = false;

    }

    public void Exit()
    {
        Debug.Log("Exiting Dead State");
    }

    public void Update()
    {
        enemyController.animator.SetBool("isDead", true);
    }
}
