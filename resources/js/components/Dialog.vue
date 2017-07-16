<template>
    <div class="dialog" :class="{hide: !message}" @click="close()">
        <div class="dialog-content" :class="{hide: !message}">
            <div class="dialog-content-header">
                <div class="dialog-content-title" v-text="title"></div>
            </div>
            <div class="dialog-content-body" v-text="message"></div>
            <div class="dialog-content-footer">
                <button type="button" @click="close()">閉じる</button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data: () => {
            return {
            }
        },
        props: ['title', 'message'],
        methods: {
            close() {
                this.$emit('close');
            },
        },
    }
</script>