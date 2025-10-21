using UnityEngine;

public class ElevatorController : MonoBehaviour
{
    public Transform elevator; 
    public float speed = 2f;
    public float upperLimit = 13.42f; 
    public float lowerLimit = 3.122f;

    private bool moveUp = false;
    private bool moveDown = false;

    void Start()
    {

    }

    void Update()
    {
       
    }

    public void MoveUp()
    {
        if (elevator.position.y < upperLimit)
        {
            elevator.Translate(Vector3.up * speed * Time.deltaTime);
        }
    }

    public void MoveDown()
    {
        if (elevator.position.y > lowerLimit)
        {
            
            elevator.Translate(Vector3.down * speed * Time.deltaTime);
        }
    }

    public void Stop()
    {
        moveUp = false;
        moveDown = false;
    }
}
