<script>
import { collapsed, toggleSidebar, sidebarWidth } from '@/components/sidebar/state'
import { faAngleDoubleLeft, faHome } from '@fortawesome/free-solid-svg-icons'
import SidebarLink from '@/components/sidebar/SidebarLink.vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

export default {
    props: {},
    components: { SidebarLink },
    setup() {
        return { collapsed, toggleSidebar, sidebarWidth, faAngleDoubleLeft, faHome }
    }
}
</script>

<template>
    <div class="sidebar" :style="{ width: sidebarWidth }">
        <h1>
            <span v-if="collapsed">
                <font-awesome-icon :icon="faHome"></font-awesome-icon>
            </span>
            <span v-else>Sidebar</span>
        </h1>

        <SidebarLink to="/" icon="faHome">Home</SidebarLink>
        <SidebarLink to="/tic-tac-toe" icon="faHome">TicTacToe</SidebarLink>
        <SidebarLink to="/coming-soon" icon="faHome">Coming Soon</SidebarLink>

        <span
            style="position: absolute; bottom: 1em"
            class="collapse-icon"
            :class="{ 'rotate-180': collapsed }"
            @click="toggleSidebar"
        >
            <font-awesome-icon :icon="faAngleDoubleLeft" />
        </span>
    </div>
</template>

<style>
:root {
    --sidebar-bg-color: #2f855a;
    --sidebar-item-hover: #38a169;
    --sidebar-item-active: #276749;
}
</style>

<style scoped>
.sidebar {
    color: white;
    background-color: var(--sidebar-bg-color);

    float: left;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    bottom: 0;
    padding: 0.5em;

    transition: 0.3s ease;

    display: flex;
    flex-direction: column;
}

.rotate-180 {
    transform: rotate(180deg);
    transition: 0.2 linear;
}
</style>