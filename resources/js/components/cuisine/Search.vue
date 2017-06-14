<template>
    <div class="search-cuisine">
        <search-header @search="search()"></search-header>
        <search-data :items="items"></search-data>
    </div>
</template>

<script>
    import SearchHeader from './SearchHeader.vue';
    import SearchData from './SearchData.vue';

    export default {
        data() {
            return {
                items: [],
            }
        },
        components: {
            searchHeader: SearchHeader,
            searchData: SearchData,
        },
        methods: {
            search(_obj) {
                this.$http.get('/recipe/api/cuisine').then(res => {
                    this.items = res.body;
                });
            }
        },
        mounted() {
            this.search();
        },
    };
</script>
