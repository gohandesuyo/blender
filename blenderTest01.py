import bpy

# デフォルトのCubeを削除
def delete_all():
    for item in bpy.context.scene.objects:
        bpy.context.scene.objects.unlink(item)

    for item in bpy.data.objects:
        bpy.data.objects.remove(item)

    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

    for item in bpy.data.materials:
        bpy.data.materials.remove(item)

delete_all()

# 頂点座標を定義
coords=[
    (-1.0, -1.0, -1.0),
    ( 1.0, -1.0, -1.0),
    ( 1.0,  1.0, -1.0),
    (-1.0,  1.0, -1.0),
    ( 0.0,  0.0,  1.0)
]

# この添字を使って面を定義
# 各面は４つの整数の並びで定義
# 三角形の面は最初の頂点と４つ目の頂点が同じになる必要
faces=[
    (2,1,0,3),
    (0,1,4,0),
    (1,2,4,1),
    (2,3,4,2),
    (3,0,4,3)
]

# 新規メッシュを作成
me          = bpy.data.meshes.new("PyramidMesh")
# メッシュでオブジェクトを作成
ob          = bpy.data.objects.new("Pyramid", me)
# オブジェクトを 3D カーソルの位置に配置
ob.location = bpy.context.scene.cursor_location
# オブジェクトをシーンにリンク
bpy.context.scene.objects.link(ob)
# メッシュの頂点、辺、面を埋めまる
me.from_pydata(coords,[],faces)
# 新たなデータでメッシュを更新
me.update(calc_edges=True)