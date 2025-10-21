using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LaserCollisionDetector : MonoBehaviour
{
    private GameObject stealthManager;
    
    // Start is called before the first frame update
    void Start()
    {
        stealthManager = GameObject.FindGameObjectWithTag("StealthManager");
    }
    
    // Update is called once per frame
    void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.tag == "Player")
        {
            stealthManager.GetComponent<StealthManager>().ApplyStealthDamage(20);
            Debug.Log(other.gameObject.tag + " stealth reduced by 20");
        }
    }
}
