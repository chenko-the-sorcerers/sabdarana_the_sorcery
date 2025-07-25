<script lang="ts">
	export let text: string = 'Memeriksa tulisan Anda...';
</script>

<div class="fixed inset-0 z-[1000] flex items-center justify-center bg-black/50">
	<div class="flex flex-col items-center space-y-4 rounded-2xl bg-white px-8 py-6 shadow-xl">
		<!-- Ganti spinner dengan gambar GIF -->
		<img src="/loading-arutala.gif" alt="Loading..." class="h-24 w-24" />
		<p class="text-center text-lg font-semibold text-blue-500">{text}</p>
	</div>
</div>
