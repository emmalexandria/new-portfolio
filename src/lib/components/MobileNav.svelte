<script>
	import EmphLink from "./EmphLink.svelte";

	import NavItem from "./NavItem.svelte";
</script>

<nav class="block md:hidden w-full px-8 pb-4">
	<ul class="flex flex-col md:flex-row items-baseline gap-4 md:gap-16">
		<NavItem href="/" title="Portfolio" />
		<NavItem href="/about" title="About" />
		<NavItem href="/contact" title="Contact" />
		<NavItem
			href="https://blog.emmalexandria.dev"
			title="Blog"
			target="_blank"
		/>
	</ul>
</nav>
