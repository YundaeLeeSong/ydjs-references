using System.Collections;
using UnityEngine;
using UnityEngine.UI;

public class StealthManager : MonoBehaviour
{
    public Image stealthBar;
    public float stealth = 100f;
    public float maxStealth = 100f;
    public float regenRate = 1f; 

    private HUD hud;
    private Menu menu;
    private bool isGameOver = false;
    private Coroutine continuousDamageCoroutine;
    private Coroutine regenCoroutine;

    void Awake()
    {
        hud = GameObject.FindGameObjectWithTag("HUD").GetComponent<HUD>();
        menu = GameObject.FindGameObjectWithTag("Menu").GetComponent<Menu>();
    }

    void Start()
    {
        stealth = 100f;
        StartStealthRegen();
    }

    void Update()
    {
        if (stealth <= 0 && !isGameOver)
        {
            Time.timeScale = 0f;
            GameObject.FindGameObjectWithTag("Menu").GetComponent<Menu>().UpdateTextState(Menu.GameState.GameOver);
            hud.Disable();
            menu.Enable();
            isGameOver = true;
            StopStealthRegen();
        }
    }

    public void GetDetected()
    {
        if (continuousDamageCoroutine == null)
        {
            continuousDamageCoroutine = StartCoroutine(ApplyContinuousDamage());
        }
    }

    public void StopDetection()
    {
        if (continuousDamageCoroutine != null)
        {
            StopCoroutine(continuousDamageCoroutine);
            continuousDamageCoroutine = null;
        }
    }

    public void SetStealth(float amount)
    {
        stealth = Mathf.Min(maxStealth, amount);
        stealthBar.fillAmount = stealth / maxStealth;
    }

    public void ApplyStealthDamage(float damage)
    {
        stealth = Mathf.Max(0f, stealth - damage);
        stealthBar.fillAmount = stealth / maxStealth;
    }

    private IEnumerator ApplyContinuousDamage()
    {
        while (true)
        {
            yield return new WaitForSeconds(2f);
            ApplyStealthDamage(50f);
        }
    }

    private void StartStealthRegen()
    {
        if (regenCoroutine == null)
        {
            regenCoroutine = StartCoroutine(PassiveStealthRegen());
        }
    }

    private void StopStealthRegen()
    {
        if (regenCoroutine != null)
        {
            StopCoroutine(regenCoroutine);
            regenCoroutine = null;
        }
    }

    private IEnumerator PassiveStealthRegen()
    {
        while (true)
        {
            yield return new WaitForSeconds(1f);
            if (stealth < maxStealth)
            {
                SetStealth(stealth + regenRate);
            }
        }
    }
}
