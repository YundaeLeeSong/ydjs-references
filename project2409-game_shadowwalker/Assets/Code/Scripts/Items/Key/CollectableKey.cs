using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CollectableKey : MonoBehaviour
{
    void OnTriggerEnter(Collider c)
    {
        if (c.gameObject.tag == "Player") {
            KeyCollector kc = c.gameObject.GetComponent<KeyCollector>();
            if (kc != null) {
                kc.ReceiveKey();
                Destroy(this.gameObject);

                Time.timeScale = 0f;
                GameObject.FindGameObjectWithTag("Menu").GetComponent<Menu>().UpdateTextState(Menu.GameState.YouWon);
                GameObject.FindGameObjectWithTag("HUD").GetComponent<CanvasGroup>().alpha = 0f;
                GameObject.FindGameObjectWithTag("HUD").GetComponent<CanvasGroup>().interactable = false;
                GameObject.FindGameObjectWithTag("HUD").GetComponent<CanvasGroup>().blocksRaycasts = false;
                GameObject.FindGameObjectWithTag("Menu").GetComponent<CanvasGroup>().alpha = 1f;
                GameObject.FindGameObjectWithTag("Menu").GetComponent<CanvasGroup>().interactable = true;
                GameObject.FindGameObjectWithTag("Menu").GetComponent<CanvasGroup>().blocksRaycasts = true;
            }
        }
    }
}
