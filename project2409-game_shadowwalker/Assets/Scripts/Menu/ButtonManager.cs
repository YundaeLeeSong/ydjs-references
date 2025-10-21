using System.Collections;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ButtonManager : MonoBehaviour
{
    private float waitTime = 0.3f;

    void Start()
    {

    }

    void Update()
    {

    }

    public void QuitGame()
    {
        StartCoroutine(WaitAndQuitGame());
    }

    IEnumerator WaitAndQuitGame()
    {
        // Temporarily unpause the game to allow the coroutine to run
        float originalTimeScale = Time.timeScale;
        Time.timeScale = 1f;
        Debug.Log("Before waiting 0.3 seconds");
        yield return new WaitForSecondsRealtime(waitTime);
        Debug.Log("After waiting 0.3 seconds");

        Time.timeScale = originalTimeScale; // Restore the original time scale
        #if UNITY_EDITOR
        UnityEditor.EditorApplication.isPlaying = false;
        #else
        Application.Quit();
        #endif
    }

    public void RestartScene()
    {
        StartCoroutine(WaitAndRestartScene());
    }

    IEnumerator WaitAndRestartScene()
    {
        // Temporarily unpause the game to allow the coroutine to run
        Time.timeScale = 1f;
        Debug.Log("Before waiting 0.3 seconds");
        yield return new WaitForSecondsRealtime(waitTime);
        Debug.Log("After waiting 0.3 seconds");

        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
        Time.timeScale = 1f; // Ensure time scale is reset after scene load
    }

    public void StartScene(string sceneName)
    {
        StartCoroutine(WaitAndStartScene(sceneName));
    }

    IEnumerator WaitAndStartScene(string sceneName)
    {
        // Temporarily unpause the game to allow the coroutine to run
        float originalTimeScale = Time.timeScale;
        Time.timeScale = 1f;
        Debug.Log("Before waiting 0.3 seconds");
        yield return new WaitForSecondsRealtime(waitTime);
        Debug.Log("After waiting 0.3 seconds");

        Time.timeScale = originalTimeScale; // Restore the original time scale
        SceneManager.LoadScene(sceneName);
    }
}
