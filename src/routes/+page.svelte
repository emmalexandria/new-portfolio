<script>
    import H2 from "$lib/components/typography/H2.svelte";
    import ProjectCard from "$lib/components/ProjectCard.svelte";
    import H1 from "$lib/components/typography/H1.svelte";
    import ProjectSection from "$lib/components/ProjectSection.svelte";
    import P from "$lib/components/typography/P.svelte";
    import { error } from "@sveltejs/kit";
    import EmphLink from "$lib/components/EmphLink.svelte";
    import Icon from "@iconify/svelte";
</script>
<section class="h-screen">
    <div class="flex flex-col w-1/2 gap-4 mx-auto items-center justify-center text-center">

    <H1>
        Web and software developer
    </H1>
    <P>I work in web and software development. I also have experience in web design, writing, typesetting, and digital content creation.</P>
    <EmphLink href="#portfolio" target="_self"><span class="flex flex-row items-center gap-2"><Icon icon="mdi:arrow-down"/>Portfolio</span></EmphLink>
    </div>


</section>

<section class="pb-8 w-3/4 mx-auto">

<H1 id="portfolio">Portfolio</H1>
<div class="w-full">
    <P>
        The following is a sampling of projects of mine that I consider finished
        or currently active. I have built much more than this, however most
        ended up being shuttered or replaced.
    </P>
</div>

<ProjectSection title="Web">
    <ProjectCard
        title="M3 Tailwind"
        links={[
            {
                href: "https://m3tw.emmalexandria.dev",
                icon: "mdi:link-variant",
            },
            {
                href: "https://github.com/emmalexandria/material-tailwind",
                icon: "mdi:github",
            },
        ]}
        tech={["devicon-plain:svelte", "mdi:tailwind"]}
        >Utility for generating a Material Design color palette and exporting it
        to the Tailwind CSS config format. Built with Material components and
        changes colour according to the generated color scheme.
    </ProjectCard>
    <ProjectCard title="Hugo blog" links={[]} tech={["devicon-plain:hugo"]}
        >Personal blog built with Hugo. Refactored and modified large amounts of
        HTML and CSS from another theme and set up multiple blog sections.</ProjectCard
    >
    <ProjectCard title="Filler Project">
        Lorem ipsum dolor sit amet bla bla etc words and description things go here 
        when this project actually exists I really need to get started on some more projects.
    </ProjectCard>
</ProjectSection>
<ProjectSection title="Terminal">
    <ProjectCard title="rrecycle" tech={["devicon-plain:rust"]}
        >Cross-platform file deletion utility with support for recycle bin and
        secure deletion through file overwrites.</ProjectCard
    >
    <ProjectCard title="fRCON" tech={["devicon-plain:rust"]}
        >RCON client with command completion and formatting for both error and
        success responses.</ProjectCard
    >
</ProjectSection>
</section>