using UnityEngine;
using TMPro;

public class ElevatorButtonInteraction : MonoBehaviour
{
    public ElevatorController elevatorController; // Reference to the ElevatorController
    public bool isUpButton = false;

    private bool playerInRange = false;
    private PlayerInputController playerInputController;
    private HUD hud;

    void Awake()
    {
        playerInputController = GameObject.FindGameObjectWithTag("Player").GetComponent<PlayerInputController>();
        hud =  GameObject.FindGameObjectWithTag("HUD").GetComponent<HUD>();
    }

    void Update()
    {
        if (playerInRange && playerInputController.IsUsing())
        {
            if (isUpButton)
            {
                elevatorController.MoveUp();
            }
            else
            {
                elevatorController.MoveDown();
            }
        }
        else
        {
            elevatorController.Stop();
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            playerInRange = true;
            hud.EnableUsePrompt();
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            playerInRange = false;
            hud.DisableUsePrompt();
        }
    }
}
