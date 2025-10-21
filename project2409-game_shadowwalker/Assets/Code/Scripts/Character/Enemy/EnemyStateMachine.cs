// Inspired by the state pattern as explained in this Unity tutorial: https://unity.com/how-to/develop-modular-flexible-codebase-state-programming-pattern
public class EnemyStateMachine {
    public IState state;

    public EnemyAlertState enemyAlertState;
    public EnemyDeadState enemyDeadState;
    public EnemyPatrolState enemyPatrolState;
    public EnemyDetectedState enemyDetectedState;

    public EnemyStateMachine(EnemyController enemyController) {
        enemyPatrolState = new EnemyPatrolState(enemyController);
        enemyDeadState = new EnemyDeadState(enemyController);
        enemyAlertState = new EnemyAlertState(enemyController);
        enemyDetectedState = new EnemyDetectedState(enemyController);

        ChangeState(enemyPatrolState);
    }

    public void ChangeState(IState newState)
    {
        if (state != null)
        {
            state.Exit();
        }
        state = newState;
        newState.Enter();
    }

    public void Update()
    {
        state.Update();
    }
}