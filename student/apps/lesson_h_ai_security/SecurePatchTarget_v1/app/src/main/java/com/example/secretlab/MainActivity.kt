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
                    PatchReviewScreen()
                }
            }
        }
    }
}

@Composable
private fun PatchReviewScreen() {
    var packageName by remember { mutableStateOf("com.example.secretlab") }
    var token by remember { mutableStateOf("ALLOW") }
    var status by remember { mutableStateOf("Waiting for integrity check") }

    Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding)
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp),
        ) {
            Text("SecurePatch Target v1", style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.Bold)
            Text("A small approval form with a fake policy check.")

            OutlinedTextField(
                value = packageName,
                onValueChange = { packageName = it },
                label = { Text("Package name") },
                modifier = Modifier.fillMaxWidth(),
                singleLine = true,
            )
            OutlinedTextField(
                value = token,
                onValueChange = { token = it },
                label = { Text("Approval token") },
                modifier = Modifier.fillMaxWidth(),
                singleLine = true,
            )

            Button(onClick = { status = if (packageName == "com.example.secretlab" && token == "ALLOW") "Approved" else "Rejected" }) {
                Text("Check patch")
            }
            Button(onClick = { status = "Request bound to app identity" }) {
                Text("Bind request")
            }
            Text(status)
        }
    }
}
