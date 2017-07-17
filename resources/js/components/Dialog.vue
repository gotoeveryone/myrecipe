<template>
    <div class="dialog" :class="{hide: !notices.message}" @click="close()">
        <div class="dialog-content" :class="{hide: !notices.message}">
            <div class="dialog-content-header">
                <div class="dialog-content-title" v-text="notices.title"></div>
            </div>
            <div class="dialog-content-body" v-html="notices.message" :class="{'field-validation-error': notices.error}"></div>
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
        props: ['notices'],
        methods: {
            close() {
                this.$emit('close');
            },
        },
    }
</script>