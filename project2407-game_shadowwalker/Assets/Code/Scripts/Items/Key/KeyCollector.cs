using UnityEngine;

public class KeyCollector : MonoBehaviour
{
    public bool hasKey = false;

    public void ReceiveKey()
    {
        hasKey = true;
        
    }
}