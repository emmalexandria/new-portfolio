<script>
    import EmphLink from "./EmphLink.svelte";
import NavItem from "./NavItem.svelte";

</script>
<nav class="p-8">

<ul class="flex flex-row items-baseline gap-16">
    <li class="mr-auto font-display font-bold">
        <a href="/">
        <h1 class=" font-bold">Emma Alexandria</h1>
        </a>
    </li>
    <NavItem href="/" title="Portfolio"/>
    <NavItem href="/about" title="About"/>
    <NavItem href="/contact" title = "Contact"/>
    <li>

    <EmphLink href="https://blog.emmalexandria.dev">Blog</EmphLink>
    </li>
</ul>
</nav>