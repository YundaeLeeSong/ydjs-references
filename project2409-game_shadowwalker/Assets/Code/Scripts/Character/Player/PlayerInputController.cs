using UnityEngine;
using UnityEngine.Events;

public class PlayerInputController : MonoBehaviour 
{
    private PlayerInput playerInput;
    private PlayerMovementController playerMovementController;
    private CharacterAnimationController characterAnimationController;
    private HUD hud;
    private Menu menu;
    private bool isUsing;
    private bool isFreezing;
    private bool isTakingDown;

    void Awake()
    {
        playerMovementController = GetComponent<PlayerMovementController>();
        characterAnimationController = GetComponent<CharacterAnimationController>();
        hud = GameObject.FindGameObjectWithTag("HUD").GetComponent<HUD>();
        menu = GameObject.FindGameObjectWithTag("Menu").GetComponent<Menu>();
        isUsing = false;
        isFreezing = false;
        playerInput = new PlayerInput();
    }
    
    void Start()
    {
        Cursor.visible = false;
        playerInput.Player.Move.performed += ctx => playerMovementController.SetMovement(ctx.ReadValue<Vector2>());
        playerInput.Player.Move.canceled += ctx => playerMovementController.SetMovement(Vector2.zero);
        playerInput.Player.Run.performed += ctx => playerMovementController.SetRunning(true);
        playerInput.Player.Run.canceled += ctx => playerMovementController.SetRunning(false);
        playerInput.Player.Jump.performed += ctx => characterAnimationController.SetJumping(true);
        playerInput.Player.Jump.canceled += ctx => characterAnimationController.SetJumping(false);
        playerInput.Player.Crouch.performed += ctx => characterAnimationController.SetCrouching();
        playerInput.Player.Takedown.performed += ctx => isTakingDown = true;
        playerInput.Player.Takedown.canceled += ctx => { 
            isTakingDown = false; 
            characterAnimationController.SetTakingDown(false); 
        };
        playerInput.Player.Use.performed += ctx => isUsing = true;
        playerInput.Player.Use.canceled += ctx => isUsing = false; 
        playerInput.Player.Menu.performed += ctx => {
            hud.Disable();
            menu.Enable();
        };
        playerInput.Player.Freeze.performed += ctx => isFreezing = !isFreezing;
    }

    void Update()
    {
        
    }

    private void OnEnable()
    {
        playerInput.Player.Enable();
    }
    private void OnDisable()
    {
        playerInput.Player.Disable();
    }

    public bool IsUsing()
    {
        return isUsing;
    }

    public bool IsFreezing()
    {
        return isFreezing;
    }

    public void SetFreezing(bool isFreezing)
    {
        this.isFreezing = isFreezing;
    }

    public bool IsTakingDown()
    {
        return isTakingDown;
    }
}