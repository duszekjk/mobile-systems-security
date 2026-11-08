package com.example.secretlab

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.secretlab.ui.theme.SecretLabTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            SecretLabTheme {
                Surface {
                    PatchQueueScreen()
                }
            }
        }
    }
}

@Composable
private fun PatchQueueScreen() {
    var jobName by remember { mutableStateOf("security-fix-1042") }
    var notes by remember { mutableStateOf("Waiting for release approval") }
    var status by remember { mutableStateOf("Queue is idle") }

    Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding)
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp),
        ) {
            Text("SecurePatch Target v2", style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.Bold)
            Text("A tiny patch queue form with fake release notes.")

            OutlinedTextField(
                value = jobName,
                onValueChange = { jobName = it },
                label = { Text("Job name") },
                modifier = Modifier.fillMaxWidth(),
                singleLine = true,
            )
            OutlinedTextField(
                value = notes,
                onValueChange = { notes = it },
                label = { Text("Notes") },
                modifier = Modifier.fillMaxWidth(),
            )

            Button(onClick = { status = "Queued $jobName for mock deployment" }) {
                Text("Queue patch")
            }
            Button(onClick = { status = "Patch approved for sandbox release" }) {
                Text("Approve")
            }
            Text(status)
        }
    }
}
