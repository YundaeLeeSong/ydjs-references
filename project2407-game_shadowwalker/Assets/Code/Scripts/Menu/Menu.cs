using TMPro;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Menu : MonoBehaviour
{
    private PlayerInput playerInput;
    private CanvasGroup canvasGroup;
    private HUD hud;

    public enum GameState
    {
        GamePaused,
        GameOver,
        YouWon,
    }
    private GameState state = GameState.GamePaused;

    void Awake()
    {
        hud = GameObject.FindGameObjectWithTag("HUD").GetComponent<HUD>();
        playerInput = new PlayerInput();
    }

    void Start()
    {
        canvasGroup = GetComponent<CanvasGroup>();
        Disable();
        playerInput.UI.Exit.performed += ctx => {
            Disable();
            hud.Enable();
        };
    }

    private void OnEnable()
    {
        playerInput.UI.Enable();
    }
    private void OnDisable()
    {
        playerInput.UI.Disable();
    }

    void Update()
    {
        string text = "Game Paused";
        switch (state)
        {
            case GameState.GamePaused:
                text = "Game Paused";
                break;
            case GameState.GameOver:
                text = "Game Over";
                break;
            case GameState.YouWon:
                text = "You Won!";
                break;
        }
        GameObject.FindGameObjectWithTag("Menu State").GetComponent<TextMeshProUGUI>().text = text;
    }

    public void RestartGame()
    {
        Time.timeScale = 1f;
        SceneManager.LoadScene("AlphaLevel");
        GameObject.FindGameObjectWithTag("StealthManager").GetComponent<StealthManager>().SetStealth(100f);
    }
    public void Tutorial()
    {
        Time.timeScale = 1f;
        SceneManager.LoadScene("GameDemo");
        GameObject.FindGameObjectWithTag("StealthManager").GetComponent<StealthManager>().SetStealth(100f);
    }

    public void QuitGame()
    {
#if UNITY_EDITOR
        UnityEditor.EditorApplication.isPlaying = false;
#else
        Application.Quit();
#endif
    }

    public void UpdateTextState(GameState gameState)
    {
        state = gameState;
    }

    public void Enable()
    {
        Cursor.visible = true;
        playerInput.Player.Disable();
        playerInput.UI.Enable();
        Time.timeScale = 0f;
        canvasGroup.alpha = 1f;
        canvasGroup.interactable = true;
        canvasGroup.blocksRaycasts = true;
    }

    public void Disable()
    {
        Cursor.visible = false;
        playerInput.Player.Enable();
        playerInput.UI.Disable();
        Time.timeScale = 1f;
        canvasGroup.alpha = 0f;
        canvasGroup.interactable = false;
        canvasGroup.blocksRaycasts = false;
    }
}
