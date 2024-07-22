<script lang="ts">
	import Icon from "@iconify/svelte";
	import type { IconLink } from "$lib";
	import LinkIcon from "./LinkIcon.svelte";

	export let title: string;
	export let src: string = "https://placehold.co/400x400";
	export let links: IconLink[] = [];
	export let tech: string[] = [];
</script>

<div class="bg-mono-100 dark:bg-mono-800 w-full p-4 flex flex-col hover-shadow">
	<img
		{src}
		class="w-full h-auto mb-2"
		width="400"
		height="400"
		alt="Placeholder"
	/>
	<span class="flex flex-row items-baseline">
		<h3 class="md:text-4xl text-2xl mb-2 mr-auto">
			{title}
		</h3>
		<span class="text-2xl flex flex-row items-center gap-4">
			{#each links as link}
				<LinkIcon linkInfo={link} />
			{/each}
		</span>
	</span>

	<p class="font-body block mb-2">
		<slot />
	</p>
	<span class="flex flex-row gap-2 block mt-auto text-2xl">
		{#each tech as t}
			<Icon icon={t} />
		{/each}
	</span>
</div>
