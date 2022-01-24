using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class enterNext : MonoBehaviour
{
    public GameObject enterDialog;
    public Text SoulNum;
    private void OnTriggerEnter2D(Collider2D collition)
    {
        if(collition.tag == "Player")
        {
            enterDialog.SetActive(true);
        }
    }

    private void OnTriggerExit2D(Collider2D collition)
    {
        if(collition.tag == "Player")
        {
            enterDialog.SetActive(false);
        }
    }
}
