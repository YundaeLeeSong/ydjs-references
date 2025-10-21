using UnityEngine;

public class CharacterAnimationController : MonoBehaviour 
{
    private Animator animator;
    private int isCrouchingHash;
    private int isJumpingHash;
    private int isTakingDownHash;
    private int horizontalVelocityHash;
    private PlayerMovementController playerMovementController;

    void Awake()
    {
        animator = GetComponent<Animator>();
        playerMovementController = GetComponent<PlayerMovementController>();
    }
    
    void Start()
    {
        isCrouchingHash = Animator.StringToHash("isCrouching");
        isJumpingHash = Animator.StringToHash("isJumping");
        isTakingDownHash = Animator.StringToHash("isTakingDown");
        horizontalVelocityHash = Animator.StringToHash("horizontalVelocity");

        SetHorizontalVelocity(0.0f);
    }

    void Update()
    {
    }

    public void SetHorizontalVelocity(float horizontalVelocity)
    {
        animator.SetFloat(this.horizontalVelocityHash, horizontalVelocity);
    }

    public void SetJumping(bool isJumping)
    {
        animator.SetBool(isJumpingHash, isJumping);
    }

    public void SetCrouching()
    {
        animator.SetBool(isCrouchingHash, !IsCrouching());
    }

    public bool IsCrouching()
    {
        return animator.GetBool(isCrouchingHash);
    }

    public void SetTakingDown(bool isTakingDown)
    {
        animator.SetBool(isTakingDownHash, isTakingDown);
    }

    public bool IsTakingDown()
    {
        return animator.GetBool(isTakingDownHash);
    }
}