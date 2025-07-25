<script lang="ts">
	export let title = 'Oops!';
	export let subtitle = 'Kamu hanya bisa akses level ini di aplikasi mobile Arutala Aksara';
	export let leftButtonText = 'Kembali';
	export let rightButtonText = 'Unduh Aplikasi';
	export let onLeftClick: () => void = () => {};
	export let onRightClick: () => void = () => {};
	export let imageArea: string = ''; // Use HTML string
	export let show = false;
</script>

{#if show}
	<div
		class="absolute top-0 left-0 z-100 flex h-full w-full items-center justify-center bg-black/50"
	>
		<div
			class="bg-color-white-solid absolute inline-flex w-[90%] max-w-[640px] flex-col items-center justify-start gap-11 rounded-3xl bg-white px-6 py-6 shadow-[0px_4px_20px_0px_rgba(0,0,0,0.10)] sm:px-8 md:px-11"
		>
			<div class="inline-flex flex-col items-center justify-between self-stretch md:flex-row">
				<div class="relative inline-flex h-52 w-56 flex-col items-center justify-center gap-2.5">
					<!-- image area -->
					{@html imageArea}
				</div>
				<div class="gap-8s inline-flex flex-1 flex-col items-end justify-end gap-4">
					<!-- title -->
					<h3
						class="justify-center self-stretch text-center font-['Poppins'] text-6xl leading-[58px] font-bold text-sky-900 md:text-right"
					>
						{title}
					</h3>
					<!-- subtitle -->
					<p
						class="justify-center self-stretch px-8 text-center font-['Roboto'] text-lg leading-relaxed font-normal text-sky-900 md:px-0 md:text-right"
					>
						{@html subtitle}
					</p>
				</div>
			</div>
			<div class="inline-flex items-center justify-center gap-16 self-stretch">
				<!-- left button -->
				<button
					class="group flex w-48 cursor-pointer items-center justify-center gap-2.5 rounded-[35px] bg-indigo-50 px-2.5 py-1 outline-1 outline-blue-400 transition-all hover:bg-blue-600"
					on:click={onLeftClick}
				>
					<div
						class="justify-center text-center font-['Roboto'] text-2xl leading-loose font-normal text-sky-500 transition-all group-hover:text-white"
					>
						{leftButtonText}
					</div>
				</button>
				<button
					class="bg-download-button flex cursor-pointer items-center justify-center gap-2.5 rounded-[35px] bg-gradient-to-br px-4 py-1 outline-1 outline-offset-[-1px] outline-blue-400 transition-all"
					on:click={onRightClick}
				>
					<!-- right button -->
					<div
						class="justify-center text-center font-['Roboto'] text-2xl leading-loose font-bold text-white"
					>
						{rightButtonText}
					</div>
				</button>
			</div>
		</div>
	</div>
{/if}

<style>
	.bg-download-button {
		position: relative;
		overflow: hidden;
		z-index: 0;
		transition: transform 0.3s ease;
	}

	.bg-download-button::before {
		content: '';
		position: absolute;
		inset: 0;
		background: linear-gradient(
			93.5deg,
			rgba(113, 224, 255, 0.8) -8.2%,
			rgba(0, 166, 255, 0.8) 50.67%,
			rgba(0, 100, 255, 0.8) 109.53%
		);
		z-index: -1;
		opacity: 1;
		transition: opacity 0.3s ease;
	}

	.bg-download-button:hover::before {
		opacity: 0.6; /* atau 0, jika ingin transparan total */
	}
</style>
