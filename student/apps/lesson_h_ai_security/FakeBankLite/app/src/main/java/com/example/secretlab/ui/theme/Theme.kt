package com.example.secretlab.ui.theme

import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val NeonLight = lightColorScheme(
    primary = Color(0xFF1F6FEB),
    onPrimary = Color(0xFFFFFFFF),
    secondary = Color(0xFFFF8C42),
    onSecondary = Color(0xFF1A120B),
    tertiary = Color(0xFF7A3FF2),
    background = Color(0xFFF7F9FC),
    surface = Color(0xFFFFFFFF),
    surfaceVariant = Color(0xFFEAF0F8),
    onSurface = Color(0xFF111827),
)

private val NeonDark = darkColorScheme(
    primary = Color(0xFF7CC4FF),
    onPrimary = Color(0xFF04131F),
    secondary = Color(0xFFFFB36B),
    onSecondary = Color(0xFF2B1600),
    tertiary = Color(0xFFC89CFF),
    background = Color(0xFF0B1020),
    surface = Color(0xFF121A31),
    surfaceVariant = Color(0xFF1A2746),
    onSurface = Color(0xFFF4F7FB),
)

@Composable
fun SecretLabTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = NeonLight,
        content = content,
    )
}
