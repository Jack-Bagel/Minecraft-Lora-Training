#include frex:shaders/api/vertex.glsl
#include frex:shaders/api/world.glsl
#include frex:shaders/lib/math.glsl
#include frex:shaders/lib/noise/noise4d.glsl

/******************************************************
  Based on "GPU-Generated Procedural Wind Animations for Trees"
  by Renaldas Zioma in GPU Gems 3, 2007
  https://developer.nvidia.com/gpugems/gpugems3/part-i-geometry/chapter-6-gpu-generated-procedural-wind-animations-trees
  
  Remake of canvas default shader for the Nether
******************************************************/

#define NOISE_SCALE 0.125

void frx_startVertex(inout frx_VertexData data) {
	#ifdef ANIMATED_FOLIAGE
		float t = frx_renderSeconds() * 0.05;

		vec3 pos = (data.vertex.xyz + frx_modelOriginWorldPos()) * NOISE_SCALE;
		float wind = snoise(vec4(pos, t)) * 0.1;

		data.vertex.x += (cos(t) * cos(t * 3) * cos(t * 5) * cos(t * 7) + sin(t * 25)) * wind;
		data.vertex.z += sin(t * 19) * wind;
	#endif
}
