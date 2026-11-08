package com.example.secretlab.lab

data class ProvenanceState(
    val signingIdentityMatchesExpected: Boolean,
    val buildLooksTampered: Boolean,
    val installTimeTrustIsSeparatedFromRuntimeTrust: Boolean,
)

data class IntegrityState(
    val verdict: String?,
    val appPackageNameMatches: Boolean,
    val requestIsBoundToAppIdentity: Boolean,
)

object TaskCompletion {
    fun task2Check(state: ProvenanceState): Boolean {
        return state.signingIdentityMatchesExpected &&
            !state.buildLooksTampered &&
            state.installTimeTrustIsSeparatedFromRuntimeTrust
    }

    fun task3Check(state: IntegrityState): Boolean {
        return state.verdict == "ALLOW" &&
            state.appPackageNameMatches &&
            state.requestIsBoundToAppIdentity
    }
}
