package com.example.secretlab.secure

/**
 * A small policy wrapper: you may only reveal the protected secret if a fresh `GateToken`
 * is provided.
 *
 * In a real app the gate would come from BiometricPrompt / device credential. Here we model
 * it as a token so the policy is testable and deterministic.
 */
class BiometricBoundSecretStore(
    private val secretBox: SecretBox,
    private val clock: () -> Long,
    private val maxTokenAgeSeconds: Long = 30,
) {
    private var encryptedSecret: ByteArray? = null

    fun setSecret(plaintextSecret: ByteArray, iv: ByteArray) {
        encryptedSecret = secretBox.encrypt(plaintextSecret, iv)
    }

    fun revealSecret(token: GateToken?): ByteArray? {
        val message = encryptedSecret ?: return null
        // TODO(L05-3): enforce the gate policy:
        // - token must be non-null
        // - token age must be <= maxTokenAgeSeconds (based on `clock()`)
        // - return null when gate conditions are not met
        return secretBox.decrypt(message)
    }
}

