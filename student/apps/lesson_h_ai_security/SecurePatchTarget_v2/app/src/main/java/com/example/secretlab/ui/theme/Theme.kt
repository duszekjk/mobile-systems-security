package com.example.secretlab.ui.theme

import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val EmberLight = lightColorScheme(
    primary = Color(0xFF7E2F1B),
    onPrimary = Color(0xFFFFF6F2),
    secondary = Color(0xFF4C3F91),
    onSecondary = Color(0xFFFFF6F2),
    tertiary = Color(0xFFB86B00),
    background = Color(0xFFFFF7F2),
    surface = Color(0xFFFFFCFA),
    surfaceVariant = Color(0xFFF1E1D8),
    onSurface = Color(0xFF231814),
)

private val EmberDark = darkColorScheme(
    primary = Color(0xFFFF9D82),
    onPrimary = Color(0xFF310B04),
    secondary = Color(0xFFC7B8FF),
    onSecondary = Color(0xFF150E2E),
    tertiary = Color(0xFFFFC46B),
    background = Color(0xFF1C1210),
    surface = Color(0xFF261815),
    surfaceVariant = Color(0xFF36221C),
    onSurface = Color(0xFFFFF4EE),
)

@Composable
fun SecretLabTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = EmberLight,
        content = content,
    )
}
