using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CollectableIceCube : MonoBehaviour
{
    private IceCollector ic;

    void Start()
    {
        ic = GameObject.FindGameObjectWithTag("Player").GetComponent<IceCollector>();
    }
    
    void OnTriggerEnter(Collider c)
    {
        if (c.gameObject.tag == "Player") {
            Debug.Log("Ice cube collected");
            ic.hasIce = true;
            Debug.Log("Ice cube received");
            GameObject.FindGameObjectWithTag("Ice Meter").GetComponent<Image>().fillAmount = 1;
            Destroy(this.gameObject);
        }
    }
}
