<script lang="ts">
	import FeatureCard from '$lib/components/FeatureCard.svelte';
	import { onMount, onDestroy } from 'svelte';
	import { scriptStore } from '$lib/stores/scriptStore';
	import { get } from 'svelte/store';

	let autoSlideInterval: ReturnType<typeof setInterval>;
	let currentScript = get(scriptStore);

	interface Card {
		id: number;
		img: string;
		title: string;
		subtitle: string;
		href: string;
	}

	let cards: Card[] = [
		{
			id: 1,
			img: '/tantangan.svg',
			title: 'Tantangan',
			subtitle:
				'Tantang diri Anda dengan tingkat kesulitan yang semakin sulit dalam penulisan aksara.',
			href: `/${currentScript}/challenge`
		},
		{
			id: 2,
			img: '/latihan.svg',
			title: 'Latihan',
			subtitle: 'Uji keterampilan menulis aksara Anda melalui berbagai latihan yang menarik.',
			href: `/${currentScript}/training`
		},
		{
			id: 3,
			img: '/praktik.svg',
			title: 'Praktik',
			subtitle: 'Berlatih langsung menulis aksara untuk meningkatkan keterampilan dasar Anda.',
			href: `/${currentScript}/practice`
		}
	];

	let isPaused = false;

	function handleMouseEnter() {
		isPaused = true;
	}

	function handleMouseLeave() {
		isPaused = false;
	}

	let positions = [-1, 0, 1];
	let prevPositions = [...positions];

	function rotateRight() {
		prevPositions = [...positions];
		positions = positions.map((p) => (p - 1 < -1 ? 1 : p - 1));
	}

	function rotateLeft() {
		prevPositions = [...positions];
		positions = positions.map((p) => (p + 1 > 1 ? -1 : p + 1));
	}

	function getZIndex(i: number): number {
		const prev = prevPositions[i];
		const curr = positions[i];
		if ((prev === -1 && curr === 1) || (prev === 1 && curr === -1)) return 30;
		if (curr === 0) return 20;
		return 10;
	}

	function getStyle(pos: number, i: number): string {
		const cardWidth = 360;
		const x = pos * cardWidth;
		const y = Math.pow(pos, 2) * 60;
		const r = pos * 15;
		const z = getZIndex(i);
		const opacity = getOpacity(i);
		const pointer = pos === 0 ? 'auto' : 'none';

		return `
		transform: translate(${x}px, ${y}px) rotate(${r}deg);
		z-index: ${z};
		opacity: ${opacity};
		pointer-events: ${pointer};
		transition: transform 0.6s cubic-bezier(0.55, 0.06, 0.68, 0.19),
		            opacity 0.6s ease;
	`;
	}

	function getOpacity(i: number): number {
		const pos = positions[i];
		return pos === 0 ? 1 : 0.5;
	}

	onMount(() => {
		autoSlideInterval = setInterval(() => {
			if (!isPaused) rotateRight();
		}, 3000);

		return () => clearInterval(autoSlideInterval);
	});

	onDestroy(() => {
		clearInterval(autoSlideInterval);
	});

	const onCardClick = (href: any) => {
		window.location = href;
	};
</script>

<svelte:head>
	<title>Sundanese Script</title>
	<meta
		name="description"
		content="Platform pembelajaran aksara Sunda interaktif dengan bantuan AI. Latihan menulis, tantangan, dan praktik aksara Sunda untuk melestarikan budaya Sunda."
	/>
	<meta
		name="keywords"
		content="aksara sunda, belajar aksara sunda, menulis aksara sunda, huruf sunda, cacarakan, kaganga, arutala aksara, pembelajaran aksara sunda, AI aksara sunda, budaya sunda"
	/>
</svelte:head>

<img class="absolute top-[162px] left-15 h-48 w-48 scale-170" src="/bg-script-ta.png" alt="" />

<img class="absolute top-[250px] right-4 h-48 w-48 scale-150" src="/bg-script-sa.png" alt="" />

<div class="relative z-10 min-h-screen w-full px-6 py-20">
	<div class="flex flex-col items-center justify-center gap-[25px] text-center">
		<h2 class="text-[40px] leading-[63.80px] font-bold text-white md:text-6xl">
			Waktunya Jadi Bagian dari Pelestarian Aksara Nusantara
		</h2>
		<p class="text-[15px] font-light text-white">
			Dengan bantuan AI, Anda bisa belajar menulis, memahami, dan menguasai aksara lokal dengan cara
			yang seru, mudah, dan memotivasi.
		</p>
	</div>

	<!-- Wrapper carousel -->
	<div
		role="group"
		class="relative mt-20 flex h-[300px] w-full items-center justify-center"
		on:mouseenter={handleMouseEnter}
		on:mouseleave={handleMouseLeave}
	>
		<!-- Tombol kiri -->
		<button
			on:click={rotateLeft}
			class="absolute left-0 z-50 flex h-10 w-10 items-center justify-center md:left-25"
		>
			<img src="/arrow-circle-left.svg" alt="left" class="h-full w-full object-contain" />
		</button>

		<!-- Card container -->
		<div class="relative flex h-[300px] w-[1100px] justify-center">
			<div class="relative flex gap-[64px]">
				{#each cards as card, i (card.id)}
					<FeatureCard
						img={card.img}
						title={card.title}
						subtitle={card.subtitle}
						position={positions[i]}
						style={getStyle(positions[i], i)}
						styleClass="absolute left-1/2 -translate-x-1/2 top-0"
						onClick={() => onCardClick(card.href)}
					/>
				{/each}
			</div>
		</div>

		<!-- Tombol kanan -->
		<button
			on:click={rotateRight}
			class="absolute right-0 z-50 flex h-10 w-10 items-center justify-center md:right-25"
		>
			<img src="/arrow-circle-right.svg" alt="right" class="h-full w-full object-contain" />
		</button>
	</div>
</div>
