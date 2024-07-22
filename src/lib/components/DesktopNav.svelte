<script>
	import EmphLink from "./EmphLink.svelte";
	import NavItem from "./NavItem.svelte";
</script>

<nav class="hidden md:block">
	<ul class="flex flex-row items-baseline md:gap-16">
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
