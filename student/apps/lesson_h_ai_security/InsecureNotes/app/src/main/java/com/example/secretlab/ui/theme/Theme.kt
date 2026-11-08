package com.example.secretlab.ui.theme

import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val InkyLight = lightColorScheme(
    primary = Color(0xFF0F3D4C),
    onPrimary = Color(0xFFF4F1EA),
    secondary = Color(0xFF7A4E2D),
    onSecondary = Color(0xFFF4F1EA),
    tertiary = Color(0xFF3B5D50),
    background = Color(0xFFF4F1EA),
    surface = Color(0xFFFFFBF5),
    surfaceVariant = Color(0xFFE8E0D7),
    onSurface = Color(0xFF1C1B1A),
)

private val InkyDark = darkColorScheme(
    primary = Color(0xFF8ED1DC),
    onPrimary = Color(0xFF05202A),
    secondary = Color(0xFFE2A76F),
    onSecondary = Color(0xFF2A1608),
    tertiary = Color(0xFF9DC7B3),
    background = Color(0xFF11171A),
    surface = Color(0xFF172126),
    surfaceVariant = Color(0xFF233137),
    onSurface = Color(0xFFF3F1EA),
)

@Composable
fun SecretLabTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = InkyLight,
        content = content,
    )
}
