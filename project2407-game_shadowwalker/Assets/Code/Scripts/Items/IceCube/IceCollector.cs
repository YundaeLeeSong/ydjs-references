using UnityEngine;

public class IceCollector : MonoBehaviour
{
    public bool hasIce = false;

    public void ReceiveIce()
    {
        hasIce = true;
    }
}