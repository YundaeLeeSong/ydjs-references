using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;

public class DemoManagerScript : MonoBehaviour
{
    // Start is called before the first frame update

    public GameObject checkpoint;
    public GameObject character;
    public GameObject step;
    public GameObject limbo;
    public GameObject enemy;
    public GameObject laserCamera;
    public GameObject ice;
    public GameObject ledge;
    public Image iceMeter;

    private List<string> objectives = new List<string>();
    public int currentObjectiveNumber = 0;

    public TextMeshProUGUI objectiveText;

    void setObjectiveText()
    {
        objectiveText.text = "Current Objective: " + objectives[currentObjectiveNumber];
    }
    void Start()
    {
        iceMeter.fillAmount = 0;
        objectives.Add("Look around using the mouse controls until you can see the golden capsule up ahead.");
        objectives.Add("Walk around with the WASD keys and pick up all three blue waypoints.");
        objectives.Add("Jump over the step using Space.");
        objectives.Add("Toggle crouch using C. Duck under the wall and pass through.");
        objectives.Add("You will see an enemy in front of you. Approach from behind and perform a stealth kill.");
        objectives.Add("Pick up the ice cube by walking up to it.");
        objectives.Add("Freeze the camera by pressing F while holding the ice cube. Escape the camera's view before it unfreezes.");
        objectives.Add("Run inside the elevator using the Left Shift toggle. Use E to go up and reach the ledge.");
        objectives.Add("Pick up the key.");
        objectives.Add("Chilling");
        setObjectiveText();
    }

    // Update is called once per frame
    void Update()
    {
        // Check for ice
        if (character.GetComponent<IceCollector>().hasIce)
        {
            iceMeter.fillAmount = 1;
        }
        
        if (checkpoint.GetComponent<ViewableCheckpoint>().playerInFront && currentObjectiveNumber == 0)
        {
            Debug.Log("Objective 0 cleared");
            currentObjectiveNumber++;
        }
        else if (currentObjectiveNumber == 1)
        {
            if (character.GetComponent<WayPointCounter>().waypointCount == 3)
            {
                Debug.Log("Objective 1 cleared");
                currentObjectiveNumber++;
            }
        }
        else if (step.GetComponent<StepCheck>().crossed && currentObjectiveNumber == 2)
        {
            Debug.Log("Objective 2 cleared");
            currentObjectiveNumber++;
        }
        else if (limbo.GetComponent<StepCheck>().crossed && currentObjectiveNumber == 3)
        {
            Debug.Log("Objective 3 cleared");
            currentObjectiveNumber++;
        }
        else if (enemy.GetComponent<EnemyController>().isDead && currentObjectiveNumber == 4)
        {
            Debug.Log("Objective 4 cleared");
            currentObjectiveNumber++;
        }
        else if (ice == null && currentObjectiveNumber == 5)
        {
            Debug.Log("Objective 5 cleared");
            currentObjectiveNumber++;
        }
        else if (laserCamera.GetComponent<LaserCamera>().isFreezing && currentObjectiveNumber == 6)
        {
            Debug.Log("Objective 6 cleared");
            currentObjectiveNumber++;
        }
        else if (ledge.GetComponent<StepCheck>().crossed && currentObjectiveNumber == 7)
        {
            Debug.Log("Objective 7 cleared");
            currentObjectiveNumber++;
        }
        setObjectiveText();
    }
}
