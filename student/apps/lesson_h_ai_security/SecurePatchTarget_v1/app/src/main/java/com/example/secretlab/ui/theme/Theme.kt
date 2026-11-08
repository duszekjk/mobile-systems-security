package com.example.secretlab.ui.theme

import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val MintLight = lightColorScheme(
    primary = Color(0xFF245B4A),
    onPrimary = Color(0xFFF6F8F3),
    secondary = Color(0xFF7E6B4E),
    onSecondary = Color(0xFFF6F8F3),
    tertiary = Color(0xFF3E5C76),
    background = Color(0xFFF2F6EF),
    surface = Color(0xFFFBFDFC),
    surfaceVariant = Color(0xFFE2E9DE),
    onSurface = Color(0xFF1B231D),
)

private val MintDark = darkColorScheme(
    primary = Color(0xFF92D8C1),
    onPrimary = Color(0xFF08231A),
    secondary = Color(0xFFD7C9A5),
    onSecondary = Color(0xFF241A08),
    tertiary = Color(0xFFA8C7E8),
    background = Color(0xFF0D1512),
    surface = Color(0xFF122019),
    surfaceVariant = Color(0xFF1B2A22),
    onSurface = Color(0xFFF0F6F1),
)

@Composable
fun SecretLabTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = MintLight,
        content = content,
    )
}
