<template>
    <div class="search-cuisine">
        <search-header @search="search"></search-header>
        <search-data :items="items"></search-data>
    </div>
</template>

<script>
    import SearchHeader from './SearchHeader.vue';
    import SearchData from './SearchData.vue';

    export default {
        props: {
            message: String,
        },
        data() {
            return {
                items: [],
                params: {},
            }
        },
        components: {
            searchHeader: SearchHeader,
            searchData: SearchData,
        },
        methods: {
            search(_data) {
                Object.keys(_data).forEach(key => {
                    this.params[key] = _data[key];
                });
                this.$http.get('/recipe/api/cuisine/', {
                    params: this.params,
                }).then(res => {
                    this.items = res.body;
                });
            }
        },
        mounted() {
            if (this.message) {
                this.$emit('dialog', {
                    title: 'メール送信完了',
                    message: this.message,
                });
            }
            this.search({});
        },
    };
</script>
