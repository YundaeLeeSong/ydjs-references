
using TMPro;
using UnityEngine;

public class HUD : MonoBehaviour
{
    TextMeshProUGUI takedownPrompt;
    TextMeshProUGUI usePrompt;
    private CanvasGroup canvasGroup;
    private bool toggled;

    void Awake()
    {
        canvasGroup = GetComponent<CanvasGroup>();
        takedownPrompt = GameObject.FindGameObjectWithTag("Takedown Prompt").GetComponent<TextMeshProUGUI>();
        usePrompt = GameObject.FindGameObjectWithTag("Use Prompt").GetComponent<TextMeshProUGUI>();
    }

    void Start()
    {
        takedownPrompt.enabled = false;
        usePrompt.enabled = false;
    }

    public void Enable()
    {
        canvasGroup.alpha = 1f;
        canvasGroup.interactable = true;
        canvasGroup.blocksRaycasts = true;
    }

    public void Disable()
    {
        canvasGroup.alpha = 0f;
        canvasGroup.interactable = false;
        canvasGroup.blocksRaycasts = false;
    }

    public void EnableTakedownPrompt()
    {
        takedownPrompt.enabled = true;
    }
    
    public void DisableTakedownPrompt()
    {
        takedownPrompt.enabled = false;
    }

    public void EnableUsePrompt()
    {
        usePrompt.enabled = true;
    }
    
    public void DisableUsePrompt()
    {
        usePrompt.enabled = false;
    }
}
