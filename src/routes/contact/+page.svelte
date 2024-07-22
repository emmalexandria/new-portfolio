<script lang="ts">
	import ContactCard from "$lib/components/ContactCard.svelte";
	import H1 from "$lib/components/typography/H1.svelte";
</script>

<svelte:head>
	<title>Contact me</title>
	<meta
		name="description"
		content="My contact information and professional accounts"
	/>
</svelte:head>

<div class="text-center w-fit mx-auto">
	<H1>Contact me</H1>
	<div
		class="flex flex-col gap-4 mt-4 mb-8 items-center w-fit mx-auto text-center"
	>
		<ContactCard
			href="https://www.github.com/emmalexandria"
			icon="mdi:github">emmalexandria</ContactCard
		><ContactCard
			href="mailto:emma.jellemabutler@gmail.com"
			icon="mdi:email">emma.jellemabutler@gmail.com</ContactCard
		>
		<ContactCard
			href="https://www.linkedin.com/in/emma-jb"
			icon="mdi:linkedin">Emma Jellema-Butler</ContactCard
		>

		<p class="font-light text-sm w-full md:w-3/4">
			If you find a social media account of mine, do not attempt to
			contact me there. I will not answer.
		</p>
	</div>
</div>
