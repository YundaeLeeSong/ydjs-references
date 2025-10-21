using UnityEngine;

public class ShieldCollector : MonoBehaviour
{
    public bool hasShield = false;

    public void ReceiveShield()
    {
        hasShield = true;
    }
}