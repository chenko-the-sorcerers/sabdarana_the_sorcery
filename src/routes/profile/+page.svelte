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
	<title>Profil Saya - Arutala Aksara</title>
	<meta name="description" content="Kelola profil dan pengaturan akun Anda di Arutala Aksara" />
</svelte:head>

<div class="min-h-screen py-12">
	<div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
		<div class="bg-white/10 backdrop-blur-md shadow rounded-lg">
			<div class="px-4 py-5 sm:p-6">
				<h1 class="text-2xl font-bold text-white mb-6">Profil Saya</h1>
				
				{#if currentUser}
					<div class="space-y-6">
						<!-- Profile Picture -->
						<div class="flex items-center space-x-6">
							{#if currentUser.user_metadata?.avatar_url}
								<img 
									src={currentUser.user_metadata.avatar_url} 
									alt="Profile" 
									class="w-24 h-24 rounded-full"
								/>
							{:else}
								<div class="w-24 h-24 rounded-full bg-sky-500 flex items-center justify-center text-white font-semibold text-3xl">
									{currentUser.email?.charAt(0).toUpperCase()}
								</div>
							{/if}
							<div>
								<h2 class="text-xl font-medium text-white">
									{currentUser.user_metadata?.display_name || currentUser.user_metadata?.full_name || 'User'}
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
										{currentUser.user_metadata?.username || currentUser.user_metadata?.display_name || '-'}
									</dd>
								</div>
								<div>
									<dt class="text-sm font-medium text-gray-400">Provider</dt>
									<dd class="mt-1 text-sm text-white capitalize">
										{currentUser.app_metadata?.provider || 'Email'}
									</dd>
								</div>
								<div>
									<dt class="text-sm font-medium text-gray-400">Bergabung</dt>
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
						<div class="border-t border-gray-600 pt-6 flex justify-between">
							<button
								type="button"
								onclick={() => goto('/javanese')}
								class="inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-white hover:bg-white/10 transition-colors"
							>
								Kembali ke Dashboard
							</button>
							<button
								type="button"
								onclick={handleLogout}
								class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 transition-colors"
							>
								Keluar
							</button>
						</div>
					</div>
				{:else}
					<div class="text-center py-12">
						<p class="text-gray-300 mb-4">Anda belum login</p>
						<a 
							href="/auth/login" 
							class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-sky-500 hover:bg-sky-600 transition-colors"
						>
							Masuk
						</a>
					</div>
				{/if}
			</div>
		</div>
	</div>
</div>