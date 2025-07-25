<script lang="ts">
	export let show: boolean;
	export let youtubeId: string = '';
	export let onClose: () => void = () => {};

	let modalEl: HTMLDivElement | null = null;

	function handleClickOutside(event: MouseEvent) {
		if (event.target === modalEl) {
			onClose();
		}
	}

	function handleKeydown(event: KeyboardEvent) {
		if (event.key === 'Enter' || event.key === ' ') {
			onClose();
		}
	}
</script>

{#if show}
	<div
		bind:this={modalEl}
		on:click={handleClickOutside}
		on:keydown={handleKeydown}
		role="button"
		tabindex="0"
		class="absolute inset-0 z-50 flex items-center justify-center bg-black/50"
	>
		<div
			class="relative aspect-video w-[90%] max-w-3xl overflow-hidden rounded-lg bg-black shadow-lg"
		>
			<iframe
				class="h-full w-full"
				title="YouTube video player"
				src={`https://www.youtube.com/embed/${youtubeId}?autoplay=1&rel=0&showinfo=0`}
				allow="autoplay; encrypted-media"
				allowfullscreen
			></iframe>
		</div>
	</div>
{/if}
