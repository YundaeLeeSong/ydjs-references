using UnityEngine;

public class PlayerColliderController : MonoBehaviour 
{
    private CharacterController characterController;
    private BoxCollider boxCollider;
    private const float StandingHeight = 1.7f;
    private const float CrouchingIdleHeight = 0.85f;
    private const float CrouchingMovingHeight = 1.4f;
    private PlayerMovementController playerMovementController;
    private CharacterAnimationController characterAnimationController;

    void Awake()
    {
        playerMovementController = GetComponent<PlayerMovementController>();
        characterController = GetComponent<CharacterController>();
        boxCollider = GetComponent<BoxCollider>();
        characterAnimationController = GetComponent<CharacterAnimationController>();
    }
    
    void Start()
    {

    }

    void Update()
    {
        ResizeCollider();
    }

    public void ResizeCollider()
    {
        if (characterAnimationController.IsCrouching() && playerMovementController.GetHorizontalVelocity() == 0f) {
            float crouchingCenter = CrouchingIdleHeight / 2;
            characterController.height = CrouchingIdleHeight;
            characterController.center = new Vector3(characterController.center.x, crouchingCenter, characterController.center.z);
            boxCollider.size =  new Vector3(boxCollider.size.x, CrouchingIdleHeight, boxCollider.size.z);
            boxCollider.center = new Vector3(boxCollider.center.x, crouchingCenter, boxCollider.center.z);
        } else if (characterAnimationController.IsCrouching() && playerMovementController.GetHorizontalVelocity() > 0f) { 
            float crouchingCenter = CrouchingMovingHeight / 2;
            characterController.height = CrouchingMovingHeight;
            characterController.center = new Vector3(characterController.center.x, crouchingCenter, characterController.center.z);
            boxCollider.size =  new Vector3(boxCollider.size.x, CrouchingMovingHeight, boxCollider.size.z);
            boxCollider.center = new Vector3(boxCollider.center.x, crouchingCenter, boxCollider.center.z);
        } else {
            float standingCenter = StandingHeight / 2;
            characterController.height = StandingHeight;
            characterController.center = new Vector3(characterController.center.x, standingCenter, characterController.center.z);
            boxCollider.size =  new Vector3(boxCollider.size.x, StandingHeight, boxCollider.size.z);
            boxCollider.center = new Vector3(boxCollider.center.x, standingCenter, boxCollider.center.z);
        }
    }

    void OnControllerColliderHit(ControllerColliderHit hit)
    {
        Rigidbody body = hit.collider.attachedRigidbody;

        // Check if the hit object has a Rigidbody and is not kinematic
        if (body != null && !body.isKinematic)
        {
            Vector3 pushDir = new Vector3(hit.moveDirection.x, 0, hit.moveDirection.z);
            body.velocity = pushDir * playerMovementController.GetHorizontalVelocity();
        }
    }
}