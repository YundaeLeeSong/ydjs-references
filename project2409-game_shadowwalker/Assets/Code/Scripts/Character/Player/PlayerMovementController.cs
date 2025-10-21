using UnityEngine;

public class PlayerMovementController : MonoBehaviour 
{
    public const float HorizontalAcceleration = 0.8f;
    public const float HorizontalDeceleration = -1.2f;
    public const float IdleVelocity = 0.0f;
    public const float WalkingVelocity = 0.4f;
    public const float RunningVelocity = 1f;

    private CharacterAnimationController characterAnimationController;
    private Vector2 movement;
    private bool isRunning;
    private float horizontalVelocity;
    private float rotationSmoothTime = 0.4f;
    private float rotationVelocity;

    void Awake()
    {
        characterAnimationController = GetComponent<CharacterAnimationController>();
    }
    
    void Start()
    {
        movement = Vector2.zero;
        horizontalVelocity = 0.0f;
        isRunning = false;
    }

    void Update()
    {
        HandleMove();    
        HandleRotation();
    } 

    private void HandleMove()
    {
        bool slowingDownFromRun = horizontalVelocity > WalkingVelocity && !isRunning;
        if (movement.magnitude == 0 || slowingDownFromRun)
        {
            horizontalVelocity = Mathf.Clamp(horizontalVelocity + HorizontalDeceleration * Time.deltaTime, IdleVelocity, RunningVelocity);
        }
        else
        {
            horizontalVelocity = Mathf.Clamp(horizontalVelocity + HorizontalAcceleration * Time.deltaTime, IdleVelocity, isRunning ? RunningVelocity : WalkingVelocity); ;
        }
        characterAnimationController.SetHorizontalVelocity(horizontalVelocity);
    }

    public void HandleRotation()
    {
        if (movement.magnitude >= 0.05f)
        {
            // Inspired by https://www.youtube.com/watch?v=4HpC--2iowE @ 11:30
            // Get angle between direction of movement and the direction the player is facing
            // Then, convert from radians to degrees
            // Then, add the world space rotation of camera transform to move in the direction the camera is facing
            float lookAtAngle = Mathf.Atan2(movement.x, movement.y) * Mathf.Rad2Deg + Camera.main.transform.eulerAngles.y;
            // Add smoothing so rotation isn't jarring
            float angle = Mathf.SmoothDampAngle(transform.eulerAngles.y, lookAtAngle, ref rotationVelocity, rotationSmoothTime);
            transform.rotation = Quaternion.Euler(0, angle, 0);
        }
    }

    public float GetHorizontalVelocity()
    {
        return horizontalVelocity;
    }

    public void SetMovement(Vector2 movement)
    {
        this.movement = movement;
    }

    public void SetRunning(bool isRunning)
    {
        this.isRunning = isRunning;
    }
}