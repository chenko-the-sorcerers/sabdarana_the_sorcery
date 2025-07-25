<script lang="ts">
	import { onMount } from 'svelte';
	import { user } from '$lib/supabase/authStore';
	import { signOut } from '$lib/supabase/auth';
	import { goto } from '$app/navigation';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();
	let currentUser = $state<any>(null);

	$effect(() => {
		currentUser = $user;
	});

	async function handleLogout() {
		await signOut();
		goto('/auth/login');
	}
</script>

<svelte:head>
	<title>Profile</title>
	<meta name="description" content="Kelola profil dan pengaturan akun Anda di Arutala Aksara" />
</svelte:head>

<div class="min-h-screen py-12">
	<div class="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8">
		<div class="rounded-lg bg-white/10 shadow backdrop-blur-md">
			<div class="px-4 py-5 sm:p-6">
				<h1 class="mb-6 text-2xl font-bold text-white">My Profile</h1>

				{#if currentUser}
					<div class="space-y-6">
						<!-- Profile Picture -->
						<div class="flex items-center space-x-6">
							{#if currentUser.user_metadata?.avatar_url}
								<img
									src={currentUser.user_metadata.avatar_url}
									alt="Profile"
									class="h-24 w-24 rounded-full"
								/>
							{:else}
								<div
									class="flex h-24 w-24 items-center justify-center rounded-full bg-sky-500 text-3xl font-semibold text-white"
								>
									{currentUser.email?.charAt(0).toUpperCase()}
								</div>
							{/if}
							<div>
								<h2 class="text-xl font-medium text-white">
									{currentUser.user_metadata?.display_name ||
										currentUser.user_metadata?.full_name ||
										'User'}
								</h2>
								<p class="text-gray-300">{currentUser.email}</p>
							</div>
						</div>

						<!-- User Info -->
						<div class="border-t border-gray-600 pt-6">
							<dl class="grid grid-cols-1 gap-x-4 gap-y-6 sm:grid-cols-2">
								<div>
									<dt class="text-sm font-medium text-gray-400">Email</dt>
									<dd class="mt-1 text-sm text-white">{currentUser.email}</dd>
								</div>
								<div>
									<dt class="text-sm font-medium text-gray-400">Username</dt>
									<dd class="mt-1 text-sm text-white">
										{currentUser.user_metadata?.username ||
											currentUser.user_metadata?.display_name ||
											'-'}
									</dd>
								</div>
								<div>
									<dt class="text-sm font-medium text-gray-400">Provider</dt>
									<dd class="mt-1 text-sm text-white capitalize">
										{currentUser.app_metadata?.provider || 'Email'}
									</dd>
								</div>
								<div>
									<dt class="text-sm font-medium text-gray-400">Join</dt>
									<dd class="mt-1 text-sm text-white">
										{new Date(currentUser.created_at).toLocaleDateString('id-ID', {
											year: 'numeric',
											month: 'long',
											day: 'numeric'
										})}
									</dd>
								</div>
							</dl>
						</div>

						<!-- Actions -->
						<div class="flex justify-between border-t border-gray-600 pt-6">
							<button
								type="button"
								onclick={() => goto('/javanese')}
								class="inline-flex items-center rounded-md border border-gray-300 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-white/10"
							>
								Back to Dashboard
							</button>
							<button
								type="button"
								onclick={handleLogout}
								class="inline-flex items-center rounded-md border border-transparent bg-red-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-red-700"
							>
								Logout
							</button>
						</div>
					</div>
				{:else}
					<div class="py-12 text-center">
						<p class="mb-4 text-gray-300">Not Authorized</p>
						<a
							href="/auth/login"
							class="inline-flex items-center rounded-md border border-transparent bg-sky-500 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-sky-600"
						>
							Login
						</a>
					</div>
				{/if}
			</div>
		</div>
	</div>
</div>
