<template>
    <div class="search-results">
        <ul class="table-header">
            <li class="table-row">
                <span class="name">メニュー</span>
                <span class="type">分類</span>
                <span class="kcal">Kcal</span>
                <span class="count">作成回数</span>
                <span class="detail-link">詳細</span>
            </li>
        </ul>
        <ul class="table-body" v-if="items">
            <li class="table-row" v-for="(item, idx) in items" :key="idx">
                <span class="name" v-text="item.name"></span>
                <span class="type" v-text="item.classification"></span>
                <span class="kcal" v-text="item.ingestion_kcal"></span>
                <span class="count" v-text="item.create_number_of_times"></span>
                <span class="detail-link">
                    <a :href="getUrl(item)">詳細を見る</a>
                </span>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        props: {
            items: Array,
        },
        data() {
            return {
            }
        },
        methods: {
            getUrl(_item) {
                return `/recipe/cuisine/edit/${_item.id}`;
            }
        },
    };
</script>
