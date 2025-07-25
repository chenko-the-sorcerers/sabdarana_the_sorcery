<script lang="ts">
	import { drawVM } from '$lib/stores/drawVM';
	import Notification from './Notification.svelte';

	export let status: boolean;
	export let show: boolean = false;
	export let text: string = '';
	export const isDesktop: boolean = false;
	export const labels: { label: string; value: string }[] = [];
	export let onNextCharacter: () => void;
	export let onCloseDialog: () => void;

	function close() {
		drawVM.update((vm) => ({
			...vm,
			status: null,
			results: []
		}));
		onCloseDialog();
	}

	const imagePath = status ? '/success.gif' : '/failed.gif';

	const heading = status ? 'Bagus!' : 'Oops!';
	const description = status
		? `Anda telah menyelesaikan karakter <b>${text}</b>, ${window.innerWidth > 768 ? '<br>' : ''} Siap untuk melanjutkan?`
		: `Sepertinya penulisan${window.innerWidth > 768 ? '<br>' : ''} Aksara Anda perlu diperbaiki!`;
	const getRightButton = () => {
		const isShort = window.innerWidth > 768;

		if (status) {
			return isShort ? 'Karakter Selanjutnya' : 'Lanjut';
		} else {
			return isShort ? 'Coba Lagi' : 'Ulangi';
		}
	};
	const rightButton = getRightButton();
</script>

<Notification
	{show}
	title={heading}
	subtitle={description}
	leftButtonText="Kembali"
	rightButtonText={rightButton}
	onLeftClick={onCloseDialog}
	onRightClick={onNextCharacter}
	imageArea={`
		<img class="h-50" src="${imagePath}" alt="" />
	`}
/>
