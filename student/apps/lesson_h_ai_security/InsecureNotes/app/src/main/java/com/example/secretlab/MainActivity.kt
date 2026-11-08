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
                    InsecureNotesScreen()
                }
            }
        }
    }
}

@Composable
private fun InsecureNotesScreen() {
    var title by remember { mutableStateOf("Team note") }
    var body by remember { mutableStateOf("Lunch moved to 13:30.") }
    var status by remember { mutableStateOf("Draft saved locally") }

    Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding)
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp),
        ) {
            Text("Insecure Notes", style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.Bold)
            Text("A simple note editor with a fake sync button.")

            OutlinedTextField(
                value = title,
                onValueChange = { title = it },
                label = { Text("Note title") },
                modifier = Modifier.fillMaxWidth(),
                singleLine = true,
            )
            OutlinedTextField(
                value = body,
                onValueChange = { body = it },
                label = { Text("Note text") },
                modifier = Modifier.fillMaxWidth(),
            )

            Button(onClick = { status = "Saved \"$title\" to fake cloud" }) {
                Text("Save note")
            }
            Button(onClick = { status = "Synced \"$title\" with mock server" }) {
                Text("Sync now")
            }
            Text(status)
        }
    }
}
