using UnityEngine;

public class EnemyDetectedState : IState
{
    public Vector3 alertPosition;
    private EnemyController enemyController;
    public EnemyDetectedState(EnemyController enemyController)
    {
        this.enemyController = enemyController;
    }

    public void Enter()
    {
        Debug.Log("Entering Detected State");
        GameObject.FindGameObjectWithTag("StealthManager").GetComponent<StealthManager>().GetDetected();
    }

    public void Exit()
    {
        Debug.Log("Exiting Detected State");
    }

    public void Update()
    {
        // Game over is handled by the StealthManager when stealth reaches zero
    }
}
